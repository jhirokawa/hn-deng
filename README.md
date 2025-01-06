# HN Who's hiring

A toy example of grabbing recent HackerNews "Who is hiring" posts and searching text with regex. I set a time limit for myself of 1 hour and started without knowing if HackerNews even had an API (though I assumed they likly did given the audience). There is obviously a lot to be improved, but a few obvious/low hanging improvements could be things like retries and backoffs on API calls. A simple CLI would also improve ergonomics ([typer] is a current favorite for me).

> [!TIP]
> Run with `jq` to get nice formatting
> ```bash
>  poetry run python hacker_news_whoishiring/hacker-news.py | jq '.'
> ```

[typer]: https://typer.tiangolo.com
