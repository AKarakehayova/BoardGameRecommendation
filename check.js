const fs = require('fs')
const file = require('./ForumCrawler/ForumCrawler/spiders/comments.json')
const axios = require('axios')
// const util = require('./util.js')

function spellcheck() {
    let content = JSON.stringify(file)
    return new Promise((resolve, reject) => {
        // util.processFile('./ForumCrawler/ForumCrawler/games.txt').then((resp) => {
        let values = Object.values(file)
        let allValues = []
        let promises = []
        for (var i = 0; i < values.length; i++) {
            promises.push(helper(values[i].comment))
        }
        Promise.all(promises).then(function (values) {
            // allValues = allValues.concat(...values)
            // content = content.replace(keys[i], response.data.corrections[`${keys[i]}`][0])
            resolve(values)
        })


    })


}

function helper(comment) {
    const instance = axios.create({
        baseURL: 'https://montanaflynn-spellcheck.p.mashape.com/',
        headers: {
            "X-Mashape-Key": "3xWp8Q7Bp9mshRsJdhAbmx0vahWJp1Zx3tCjsnJWdfcxdKlHgJ",
            "X-RapidAPI-Key": "WHsxLZY8kPmshpr59TlLzKFTQCY5p18QC0Sjsn7rT4POVTOYQw",
            "Accept": "application/json"
        }
    })
    return new Promise((resolve, reject) => {
        instance.get('check/', { params: { text: comment } }).then(function (response) {
            let keys = Object.keys(response.data.corrections)
            let toReplace = []
            let obj = {}
            let fixed
            for (var i = 0; i < keys.length; i++) {
                let trimmedKey = keys[i].replace('"', '') //cleanup
                trimmedKey = keys[i].replace('{', '') //cleanup
                if (!(trimmedKey.charAt(0) === trimmedKey.charAt(0).toUpperCase())) {
                    fixed = fixed ? fixed.replace(keys[i], response.data.corrections[`${keys[i]}`][0]) : comment.replace(keys[i], response.data.corrections[`${keys[i]}`][0])
                }
            }
            if (fixed) {
                obj[`${comment}`] = `${fixed}`
            }
            resolve(obj)

            //todo it can be game name with small first letter - check for game names
        })
    })
}
module.exports = {
    spellcheck: spellcheck
}
