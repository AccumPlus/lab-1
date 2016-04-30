class Controller:

    @staticmethod
    def __getListNum(curInd, maxNum):

        line = []

        if curInd > maxNum:
            curInd = int(maxNum)
        elif curInd < 1:
            curInd = 1

        if maxNum > 0:
            tr = []
            if curInd - 1 > 0:
                tr.append(curInd - 1)
            tr.append(curInd)
            if curInd + 1 <= maxNum:
                tr.append(curInd + 1)

            line.extend(tr)

            if (tr[0] != 1):
                line.insert(0, 1)

            if (tr[0] > 2):
                line.insert(1, '..')

            if (tr[-1] != maxNum):
                line.append(maxNum)

            if (maxNum - tr[-1] > 1):
                line.insert(len(line) - 1, '..')

        return line

    @staticmethod
    def getHtml(curInd, maxNum):
        listNum = Controller.__getListNum(curInd, maxNum)
        html = '<p>'

        for elem in listNum:
            if elem == '..':
                link = elem
            else:
                link = "<a href = 'http://localhost:"\
                       "5000/?num={0}'>{0}</a>".format(elem)
            html += '&nbsp;' + link

        html += '</p>'

        return html
