import urllib2
import urllib


def open_url(url):
    response = urllib2.urlopen(url)
    web_content = response.read()

    return web_content.split()


def main():

    for episode in range(65, 349):
        url = "http://animehd47.com/anime-movie/naruto-shippuuden-dub/s1-m%s/" % episode

        for line in open_url(url):
            if "googleusercontent.com" in line:
                player_line = line
                video_url = ":".join(player_line.split(",")[0].split(":")[1:3])
                video_url = video_url[1:-1]
                video_url = video_url.replace("\\", "")
                print "About to download Episode: %s" % episode
                print "URL: %s" % video_url

                dl = urllib2.urlopen(video_url)
                with open("Naturo_episode_%s.mp4" % episode, "wb") as file:
                    file.write(dl.read())

                #dl = urllib.urlopen(video_url, "Natruto_Episode_%s.mp4" % episode)
                #print dl


if __name__ == "__main__":
    main()
