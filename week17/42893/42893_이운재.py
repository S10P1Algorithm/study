from collections import defaultdict


def solution(word, pages):
    # [url, link, 기본점수, idx, 매칭 점수]
    web = []
    word = word.lower()
    link_dic = dict()
    connect_dic = defaultdict(list)

    for i in range(len(pages)):
        html = pages[i].split('\n')

        # head 태그 처리
        # url 구하기
        head = html[html.index('<head>') + 1:html.index('</head>  ')]
        for meta in head:
            if '<meta property="og:url" content="' in meta:
                url = meta[meta.index('https://'):meta.index('"/>')]
                break

        # body 태그 처리
        # 외부 링크와 기본 점수 구하기
        body = html[html.index('<body>') + 1:html.index('</body>')]
        link = []
        basic_score = 0
        for line in body:
            line = line.lower()

            w = ''
            while '<a href="' in line:
                text = line[:line.index('<a href="')]

                # text에 word 있는지 탐색
                for c in text:
                    if c.isalpha():
                        w += c
                    else:
                        if w == word:
                            basic_score += 1
                        w = ''
                if w == word:
                    basic_score += 1
                w = ''

                # 외부 링크 구하고, 남은 text 부분을 line에 담기
                line = line[line.index('<a href="') + 9:]
                new_link = line[:line.index('"')]
                line = line[line.index('"'):]
                link.append(new_link)
                connect_dic[new_link].append(url)

            # line에 담긴 텍스트에서 word 단어 개수 구하기
            for c in line:
                if c.isalpha():
                    w += c
                else:
                    if w == word: basic_score += 1
                    w = ''
            if w == word: basic_score += 1

        link_dic[url] = i
        web.append([url, link, basic_score, i])

    for i in range(len(web)):
        link_score = 0
        for link in connect_dic[web[i][0]]:
            if link in link_dic:
                link_score += (web[link_dic[link]][2] / len(web[link_dic[link]][1]))
        web[i].append(link_score + web[i][2])

    web.sort(key=lambda x: (-x[4], x[3]))

    return web[0][3]