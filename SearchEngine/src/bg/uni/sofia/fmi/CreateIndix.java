package bg.uni.sofia.fmi;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.StringField;
import org.apache.lucene.document.TextField;
import org.apache.lucene.document.Field.Store;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.index.IndexWriterConfig.OpenMode;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.json.JSONArray;
import org.json.JSONObject;

public class CreateIndix {
	public static void main(String[] args) throws IOException {
		StandardAnalyzer standardAnalyzer = new StandardAnalyzer();
		String inputFilePath = "../ForumCrawler/comments.json";
		String outputDir = "./output";

		Directory directory = FSDirectory.open(Paths.get(outputDir));
		IndexWriterConfig config = new IndexWriterConfig(standardAnalyzer);
		config.setOpenMode(OpenMode.CREATE);
		IndexWriter writer = new IndexWriter(directory, config);

		Document document = null;

		List<String> lines = Files.readAllLines(Paths.get(inputFilePath), StandardCharsets.UTF_8);
		String result = String.join("\n", lines);
		JSONArray json = new JSONArray(result);
		int size = json.length();
		for (int i = 0; i < size; i++) {
			JSONObject object = json.getJSONObject(i);
			String user = object.getString("user");
			String comment = object.getString("comment");
			document = new Document();
			document.add(new StringField("user", user, Store.YES));
			document.add(new TextField("comment", comment, Store.YES));
			writer.addDocument(document);
		}
		writer.close();
	}
}
