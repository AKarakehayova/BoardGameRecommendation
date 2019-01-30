var fs = require('fs'),
        readline = require('readline')

function processFile(inputFile) {
        var instream = fs.createReadStream(inputFile)
        var outstream = new (require('stream'))()
        var rl = readline.createInterface(instream, outstream);
        let array = []
    return new Promise((resolve, reject) => {
        rl.on('line', function (line) {
            array.push(line)
        });

        rl.on('close', () => resolve(array))
    })
}
module.exports = {
    processFile: processFile
}