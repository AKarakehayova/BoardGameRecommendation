package bg.uni.sofia.fmi;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

public class ParseQuery {
	public static final String OUTPUT_DIR = "./output";
	public static final String QUERY_FIELD = "comment";

	public static void main(String[] args) throws Exception {

		if (args.length != 1) {
			System.out.println("You should provide a query");
			System.exit(1);
		}
		IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(OUTPUT_DIR)));
		IndexSearcher searcher = new IndexSearcher(reader);
		Analyzer analyzer = new StandardAnalyzer();

		QueryParser parser = new QueryParser(QUERY_FIELD, analyzer);

		String line = args[0];

		line = line.trim();

		Query query = parser.parse(line);
		doParseFile(searcher, query, line);

//		String[] comments = doParseArray(searcher, query, line);
//		for (String comment : comments) {
//			System.out.println(comment);
//		}

	}

	public static void doParseFile(IndexSearcher searcher, Query query, String queryString) throws Exception {
		String fileName = queryString + ".txt";
		PrintWriter writer  = new PrintWriter(Files.newBufferedWriter(Paths.get(fileName), StandardCharsets.UTF_8,
				StandardOpenOption.CREATE));

		TopDocs result = searcher.search(query, 200);
		ScoreDoc[] hits = result.scoreDocs;
		int size = hits.length;
		for (int i = 0; i < size; i++) {
			String comment = searcher.doc(hits[i].doc).get("comment");
			writer.println(comment.trim());
		}
		writer.flush();
		writer.close();
	}

	public static String[] doParseArray(IndexSearcher searcher, Query query, String queryString) throws Exception {
		TopDocs result = searcher.search(query, 200);
		ScoreDoc[] hits = result.scoreDocs;
		int size = hits.length;
		String[] output = new String[size];
		for (int i = 0; i < size; i++) {
			String comment = searcher.doc(hits[i].doc).get("comment");
			output[i] = comment.trim();
		}
		return output;
	}
}
