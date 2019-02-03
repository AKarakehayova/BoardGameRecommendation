const { exec } = require('child_process');
function getComments(game) {
        process.chdir('./SearchEngine');
        exec(`java -cp bin:libs/json-20180813.jar:libs/lucene-analyzers-common-7.6.0.jar:libs/lucene-core-7.6.0.jar:libs/lucene-queryparser-7.6.0.jar bg.uni.sofia.fmi.ParseQuery "${game}"`, (err, stdout, stderr) => {
            if (err) {
                console.log(err)
                return;
            }

            console.log(`stdout: ${stdout}`);
            console.log(`stderr: ${stderr}`);
        })
}

module.exports = {
    getComments: getComments
}