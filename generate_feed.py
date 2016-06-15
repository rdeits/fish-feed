import datetime as dt
import PyRSS2Gen as rss2gen
import os
import json
import glob

url_base = "http://192.168.0.100:8000/"

def main():
    items = []

    for folder in sorted(os.listdir(os.path.join('build', 'audio')), reverse=True):
        filename = glob.glob(os.path.join('build', 'audio', folder, '*.mp3'))[0]
        info = json.load(open(filename.replace('.mp3', '.info.json')))
        link = url_base + filename[len('build/'):]
        items.append(rss2gen.RSSItem(
            title=info['title'],
            link=link,
            description=info['description'],
            guid=rss2gen.Guid(link),
            pubDate=dt.datetime.strptime(info['upload_date'], '%Y%m%d'),
            enclosure=rss2gen.Enclosure(link, length=os.stat(filename).st_size, type="audio/mpeg")
            ))

    rss = rss2gen.RSS2(
        title="No Such Thing as the News",
        link="",
        description="No Such Thing as the News",
        lastBuildDate=dt.datetime.now(),
        items=items
        )

    rss.write_xml(open("build/rss.xml", "w"))

if __name__ == '__main__':
    main()
