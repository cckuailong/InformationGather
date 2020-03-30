from lib.decoder import load
import sys


class Navigator:
    def __init__(self):
        self.conf = None
        self.head = None
        self.content = None

    # get config
    def getConf(self):
        conf_file_path = sys.path[0] + "/config.toml"
        self.conf = load(conf_file_path)

    def getHead(self):
        with open(sys.path[0]+"/head_template.html", encoding="utf8") as f:
            head_cont = f.read()
        split_c = "<!-- / FB Open Graph -->"
        tmp = head_cont.split(split_c)
        root = self.conf["root"]
        self.head = "{}{}{}".format(tmp[0],split_c,
        tmp[1].format(url=root["url"], title=root["title"], desc=root["desc"], image=root["image"]))

    def getContent(self):
        



if __name__ == "__main__":
    navigator = Navigator()
    navigator.getConf()
    navigator.getHead()
    print(navigator.head)
