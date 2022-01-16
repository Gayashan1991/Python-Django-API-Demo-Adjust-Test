class QueryFormatter:
    def __init__(self):
        print("")

    def format_groupby(self, paramDict_):
        groupby_ = ''
        for item in paramDict_["groupb"]:
            groupby_ = groupby_ + item + ', '

        print(groupby_)