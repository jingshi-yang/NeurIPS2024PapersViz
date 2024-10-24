import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS

def count_affiliation(papers):
    # count different affiliations
    affiliations = {}
    for paper in papers:
        for author in paper['authors']:
            if author['affiliation'] not in affiliations:
                affiliations[author['affiliation']] = 0
            affiliations[author['affiliation']] += 1
    # merge affiliations containing stanford:
    for affiliation in affiliations:
        if 'stanford' in affiliation.lower() and affiliation != 'Stanford University':
            affiliations['Stanford University'] += affiliations[affiliation]

    # merge affiliations containing google:
    for affiliation in affiliations:
        if 'google' in affiliation.lower() and affiliation != 'Google':
            affiliations['Google'] += affiliations[affiliation]

    # merge affiliations containing pku:
    for affiliation in affiliations:
        if 'peking' in affiliation.lower() and affiliation != 'Peking University':
            affiliations['Peking University'] += affiliations[affiliation]

    # merge affiliations containing thu:
    for affiliation in affiliations:
        if 'tsinghua' in affiliation.lower() and affiliation != 'Tsinghua University':
            affiliations['Tsinghua University'] += affiliations[affiliation]

    # merge affiliations containing cmu:
    for affiliation in affiliations:
        if ('cmu' in affiliation.lower() or 'carnegie mellon University' in affiliation.lower()) and affiliation != 'Carnegie Mellon University':
            affiliations['Carnegie Mellon University'] += affiliations[affiliation]

    # merge affiliations containing oxford:
    for affiliation in affiliations:
        if 'oxford' in affiliation.lower() and affiliation != 'University of Oxford':
            affiliations['University of Oxford'] += affiliations[affiliation]

    # merge affiliations containing MIT:
    for affiliation in affiliations:
        if 'MIT' in affiliation and affiliation != 'Massachusetts Institute of Technology':
            affiliations['Massachusetts Institute of Technology'] += affiliations[affiliation]

    # merge affiliations containing Deepmind:
    for affiliation in affiliations:
        if 'deepmind' in affiliation.lower() and affiliation != 'DeepMind':
            affiliations['DeepMind'] += affiliations[affiliation]

    # merge affiliations containing ZJU:
    for affiliation in affiliations:
        if 'zhejiang university' in affiliation.lower() and affiliation != 'Zhejiang University':
            affiliations['Zhejiang University'] += affiliations[affiliation]

    # merge affiliations containing Microsoft:
    for affiliation in affiliations:
        if 'microsoft' in affiliation.lower() and affiliation != 'Microsoft':
            affiliations['Microsoft'] += affiliations[affiliation]

    # merge affiliations containing Shanghai Jiao Tong University:
    for affiliation in affiliations:
        if ('shanghai jiao tong university' in affiliation.lower() or 'shanghai jiaotong university' in affiliation.lower()) and affiliation != 'Shanghai Jiao Tong University':
            affiliations['Shanghai Jiao Tong University'] += affiliations[affiliation]
    affiliations['Shanghai Jiao Tong University'] += 2

    # merge affiliations containing princeton:
    for affiliation in affiliations:
        if 'princeton' in affiliation.lower() and affiliation != 'Princeton University':
            affiliations['Princeton University'] += affiliations[affiliation]

    # merge affiliations containing ustc:
    for affiliation in affiliations:
        if ('university of science and technology of china' in affiliation.lower() or 'ustc' in affiliation.lower()) and affiliation != 'University of Science and Technology of China':
            affiliations['University of Science and Technology of China'] += affiliations[affiliation]
    affiliations['University of Science and Technology of China'] -= 3

    # merge affiliations containing nus:
    for affiliation in affiliations:
        if 'national university of singapore' in affiliation.lower() and affiliation != 'National University of Singapore':
            affiliations['National University of Singapore'] += affiliations[affiliation]

    # merge affiliations containing berkeley:
    for affiliation in affiliations:
        if 'berkeley' in affiliation.lower() and affiliation != 'University of California, Berkeley':
            affiliations['University of California, Berkeley'] += affiliations[affiliation]

    del affiliations['None']
    del affiliations['MIT']
    del affiliations['Tsinghua University, Tsinghua University']
    del affiliations['']
    # del all the affiliations merged above

    # sort the affiliations by count
    affiliations = sorted(affiliations.items(), key=lambda x: x[1], reverse=True)
    # write all affiliations into file
    with open('affiliations.txt', 'w') as f:
        for affiliation in affiliations:
            f.write(f'{affiliation[0]}: {affiliation[1]}\n')
    affiliation_plot(affiliations, 'affliations.png', 'Affiliation Published Papers')


def affiliation_plot(affiliations, fig_name, plt_title):
    affiliations = affiliations[:10]
    affiliations = list(zip(*affiliations))

    affiliations[0] = list(affiliations[0])
    affiliations[1] = list(affiliations[1])
    affiliations[0].reverse()
    affiliations[1].reverse()

    affiliations[0] = [affiliation.replace('University', 'Univ.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Institute', 'Inst.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace(' of ', ' ') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('and', '&') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Science', 'Sci.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Technology', 'Tech.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('California', 'Calif.') for affiliation in affiliations[0]]
    affiliations[0] = [affiliation.replace('Massachusetts', 'Mass.') for affiliation in affiliations[0]]

    plt.figure(figsize=(20, 8), dpi=80)
    b=plt.barh(range(10), affiliations[1], height=0.8)

    plt.yticks(range(10), affiliations[0])

    for rect in b:
        w = rect.get_width()
        plt.text(w,rect.get_y()+rect.get_height()/2, '%d'%int(w), ha='left', va='center')

    plt.grid(alpha=0.4)
    plt.title(plt_title)
    plt.xlabel('Published Paper')
    plt.ylabel('Affiliation')
    plt.savefig(fig_name)
    plt.show()


def count_first_affiliations(papers):
    # count different affiliations
    affiliations = {}
    for paper in papers:
        author = paper['authors'][0]
        if author['affiliation'] not in affiliations:
            affiliations[author['affiliation']] = 0
        affiliations[author['affiliation']] += 1

    # merge affiliations containing stanford:
    for affiliation in affiliations:
        if 'stanford' in affiliation.lower() and affiliation != 'Stanford University':
            affiliations['Stanford University'] += affiliations[affiliation]

    # merge affiliations containing google:
    for affiliation in affiliations:
        if 'google' in affiliation.lower() and affiliation != 'Google':
            affiliations['Google'] += affiliations[affiliation]

    # merge affiliations containing pku:
    for affiliation in affiliations:
        if 'peking' in affiliation.lower() and affiliation != 'Peking University':
            affiliations['Peking University'] += affiliations[affiliation]

    # merge affiliations containing thu:
    for affiliation in affiliations:
        if 'tsinghua' in affiliation.lower() and affiliation != 'Tsinghua University':
            affiliations['Tsinghua University'] += affiliations[affiliation]

    # merge affiliations containing cmu:
    for affiliation in affiliations:
        if ('cmu' in affiliation.lower() or 'carnegie mellon University' in affiliation.lower()) and affiliation != 'Carnegie Mellon University':
            affiliations['Carnegie Mellon University'] += affiliations[affiliation]

    # merge affiliations containing oxford:
    for affiliation in affiliations:
        if 'oxford' in affiliation.lower() and affiliation != 'University of Oxford':
            affiliations['University of Oxford'] += affiliations[affiliation]

    # merge affiliations containing MIT:
    for affiliation in affiliations:
        if 'MIT' in affiliation and affiliation != 'Massachusetts Institute of Technology':
            affiliations['Massachusetts Institute of Technology'] += affiliations[affiliation]

    # merge affiliations containing Deepmind:
    for affiliation in affiliations:
        if 'deepmind' in affiliation.lower() and affiliation != 'DeepMind':
            affiliations['DeepMind'] += affiliations[affiliation]

    # merge affiliations containing ZJU:
    for affiliation in affiliations:
        if 'zhejiang university' in affiliation.lower() and affiliation != 'Zhejiang University':
            affiliations['Zhejiang University'] += affiliations[affiliation]

    # merge affiliations containing Microsoft:
    for affiliation in affiliations:
        if 'microsoft' in affiliation.lower() and affiliation != 'Microsoft':
            affiliations['Microsoft'] += affiliations[affiliation]

    # merge affiliations containing Shanghai Jiao Tong University:
    for affiliation in affiliations:
        if ('shanghai jiao tong university' in affiliation.lower() or 'shanghai jiaotong university' in affiliation.lower()) and affiliation != 'Shanghai Jiao Tong University':
            affiliations['Shanghai Jiao Tong University'] += affiliations[affiliation]

    # merge affiliations containing princeton:
    for affiliation in affiliations:
        if 'princeton' in affiliation.lower() and affiliation != 'Princeton University':
            affiliations['Princeton University'] += affiliations[affiliation]

    # merge affiliations containing ustc:
    for affiliation in affiliations:
        if ('university of science and technology of china' in affiliation.lower() or 'ustc' in affiliation.lower()) and affiliation != 'University of Science and Technology of China':
            affiliations['University of Science and Technology of China'] += affiliations[affiliation]

    # merge affiliations containing nus:
    for affiliation in affiliations:
        if 'national university of singapore' in affiliation.lower() and affiliation != 'National University of Singapore':
            affiliations['National University of Singapore'] += affiliations[affiliation]

    # merge affiliations containing berkeley:
    for affiliation in affiliations:
        if 'berkeley' in affiliation.lower() and affiliation != 'University of California, Berkeley':
            affiliations['University of California, Berkeley'] += affiliations[affiliation]

    del affiliations['MIT']
    del affiliations['Tsinghua University, Tsinghua University']
    del affiliations['None']
    del affiliations['']

    # sort the affiliations by count
    affiliations = sorted(affiliations.items(), key=lambda x: x[1], reverse=True)

    # write all affiliations into file
    with open('firsts_affiliations.txt', 'w') as f:
        for affiliation in affiliations:
            f.write(f'{affiliation[0]}: {affiliation[1]}\n')

    affiliation_plot(affiliations, 'first_affiliations.png' ,'Affiliations as First Author Published Papers')


def count_authors(papers):
    authors = {}
    for paper in papers:
        for author in paper['authors']:
            if author['name'] not in authors:
                authors[author['name']] = 0
            authors[author['name']]+=1
    authors = sorted(authors.items(), key=lambda x:(x[1],x[0]), reverse=True)
    return authors


def count_first_authors(papers):
    authors = {}
    for paper in papers:
        author = paper['authors'][0]
        if author['name'] not in authors:
            authors[author['name']] = 0
        authors[author['name']]+=1
    authors = sorted(authors.items(), key=lambda x:(x[1],x[0]), reverse=True)
    return authors


def prev_nips_data():
    df = pd.read_json("nipsPrev.json", lines=True)
    sns.set_context({'figure.figsize':[20, 20]})
    sns.set_style('whitegrid',rc={'axes.labelsize': 20})
    s1=sns.barplot(x="Year",
                   y="Total",
                   data=df)
    s2=sns.barplot(x="Year",
                   y="Accept",
                   data=df)
    s1.set_xlabel("Conference Year", fontsize=20)
    s1.set_ylabel("Papers", fontsize=20)
    s1.set_title('Previous NeurIPS Received Papers and Accepted Papers', fontsize=20)
    show_values(s1, space=0.02)
    show_values(s2, space=0.02)
    plt.savefig('Previous NeurIPS Received Papers and Accepted Papers.png')
    plt.show()
    print(df)


def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.0f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.0f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)


def create_word_cloud(papers):
    titles = ''
    stopword = {'Learning', 'Model', 'Based', 'via', 'Toward', 'Models', 'using', 'Deep', 'Improving'}
    for paper in papers:
        titles+=(paper['title'])
        titles+=' '
    stopwords = set(STOPWORDS).union(stopword)
    cloud = WordCloud(width=1200,
                      height=900,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=12).generate_from_text(titles)
    plt.figure(figsize = (12, 9), facecolor = None)
    plt.axis("off")
    plt.imshow(cloud)
    plt.tight_layout(pad = 0)
    plt.savefig('wordcloud.png')
    plt.show()






def main():
    papers = []
    with open('nips2024.json', 'r') as f:
        # read line by line and process
        for line in f:
            paper = json.loads(line)
            # do something with paper
            papers.append(paper)
    print(len(papers))
    count_affiliation(papers)
    count_first_affiliations(papers)
    first_authors = count_first_authors(papers)
    authors = count_authors(papers)
    print(authors[:10])
    print(first_authors[:10])

    prev_nips_data()

    create_word_cloud(papers)


    print('done')


if __name__ == '__main__':
    main()
