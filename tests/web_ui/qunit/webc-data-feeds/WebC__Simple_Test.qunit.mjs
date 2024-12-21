import WebC__Hacker_News from "../../../../cbr_custom_data_feeds/web_ui/js/webc-data-feeds/hacker-news/WebC__Hacker_News.mjs";
const { module, test , only} = QUnit

module('WebC__Hacker_News', (hooks)=>{

    let host_div, webc_hacker_news

    // test('find dependency', async (assert)=>{
    //
    //     const result = await fetch('../../../../cbr_custom_data_feeds/web_ui/js/webc-data-feeds/hacker-news/WebC__Hacker_News.mjs')
    //     console.log(result.status)
    //     console.log(WebC__Hacker_News.create())
    //     assert.ok(1)
    // })
    hooks.before(async (assert)=> {
        const timeout= 500
        assert.timeout(timeout)
        host_div = document.createElement('div')
        document.body.appendChild(host_div)
        webc_hacker_news = host_div.appendChild(WebC__Hacker_News.create())
        await webc_hacker_news.wait_for__component_ready(timeout)
    })

    hooks.after(async ()=> {
        webc_hacker_news.remove()
        host_div.remove()
    })

    test('ctor', async (assert) => {
        const feed_data = webc_hacker_news.feed_data
        const articles =  webc_hacker_news.articles
        assert.equal(feed_data.title, 'The Hacker News')
        assert.equal(articles.length , 50              )
    })

    test('html', async (assert) => {
        const h2_title = webc_hacker_news.title
        assert.equal(h2_title.innerText, 'The Hacker News Feed')
    })
})