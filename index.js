const fs = require('fs')
const file = require('./ForumCrawler/comments.json')
const axios = require('axios')
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
for (var i = 0; i < values.length - 40; i++) {
    instance.get('check/', { params: { text: values[i] } }).then(function (response) {
        content.replace(response.data.original, response.data.suggestion)
    })
        .catch(function (err) {
            console.log(err)
        })
}
fs.writeFile('testAPI.json', content)


