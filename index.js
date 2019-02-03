const fs = require('fs')
const spellcheck = require('./check')
const comments = require('./getCommentsForGame')
const file = require('./ForumCrawler/ForumCrawler/spiders/comments.json')
let content = JSON.stringify(file)
spellcheck.spellcheck().then((result) => {
    for (var i = 0; i < result.length; i++) {
        let key = Object.keys(result[i])[0]
        let value = Object.values(result[i])[0]
        content = content.replace(key, value)
    }
    fs.writeFileSync('./spellcheck.json', content)
})

comments.getComments("Blood Rage")