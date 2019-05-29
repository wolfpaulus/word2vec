# word2vec


English word vectors can be found here:

https://fasttext.cc/docs/en/english-vectors.html
 Memory usage and load-time can be reduced, by creating a smaller vector file like so:
 cat wiki-news-300d-1M.vec | head -n 50001 | tail -n 50000 > vectors50k.vec
git init