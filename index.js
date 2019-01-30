const fs = require('fs')
const file = require('./ForumCrawler/ForumCrawler/comments.json')
const axios = require('axios')
const util = require('./util.js')
util.processFile('./ForumCrawler/ForumCrawler/games.txt').then((resp)=>{
const instance = axios.create({
    baseURL: 'https://montanaflynn-spellcheck.p.mashape.com/',
    headers: {
        "X-Mashape-Key": "3xWp8Q7Bp9mshRsJdhAbmx0vahWJp1Zx3tCjsnJWdfcxdKlHgJ",
        "X-RapidAPI-Key": "WHsxLZY8kPmshpr59TlLzKFTQCY5p18QC0Sjsn7rT4POVTOYQw",
        "Accept": "application/json"
    }
})
let values = Object.values(file)
let content = JSON.stringify(file)
for (var i = 0; i < values.length - 175; i++) {
    instance.get('check/', { params: { text: values[i] } }).then(function (response) {
        let keys = Object.keys(response.data.corrections)
        for(var i = 0; i < keys.length; i++){
            let trimmedKey = keys[i].replace('"', '') //cleanup
            trimmedKey = keys[i].replace('{', '') //cleanup
            if(!(trimmedKey.charAt(0) === trimmedKey.charAt(0).toUpperCase())){
                content.replace(keys[i], response.data.corrections[`${keys[i]}`][0])
            }
            //todo it can be game name with small first letter - check for game names
        }
        // content.replace(response.data.original, response.data.suggestion)
    })
        .catch(function (err) {
            console.log(err)
        })
}

})
.catch((err)=>{
    console.log(err)
})

// fs.writeFile('testAPI.json', content)


