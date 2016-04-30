''' Класс, обрабатывающий запросы от сервера '''


class Controller:
    ''' Класс, обрабатывающий запросы от сервера '''

    @staticmethod
    def __get_list_num(cur_ind, max_num):

        line = []

        if cur_ind > max_num:
            cur_ind = int(max_num)
        elif cur_ind < 1:
            cur_ind = 1

        if max_num > 0:
            troika = []
            if cur_ind - 1 > 0:
                troika.append(cur_ind - 1)
            troika.append(cur_ind)
            if cur_ind + 1 <= max_num:
                troika.append(cur_ind + 1)

            line.extend(troika)

            if troika[0] != 1:
                line.insert(0, 1)

            if troika[0] > 2:
                line.insert(1, '..')

            if troika[-1] != max_num:
                line.append(max_num)

            if max_num - troika[-1] > 1:
                line.insert(len(line) - 1, '..')

        return line

    @staticmethod
    def get_html(cur_ind, max_num):
        ''' Метод получения html-кода строки номеров страниц '''
        list_num = Controller.__get_list_num(cur_ind, max_num)
        html = '<p>'

        for elem in list_num:
            if elem == '..':
                link = elem
            else:
                link = "<a href = 'http://localhost:"\
                       "5000/?num={0}'>{0}</a>".format(elem)
            html += '&nbsp;' + link

        html += '</p>'

        return html
