FROM node:14-slim

# パッケージインストール用
RUN { \
        echo " apt update \\"; \
        # 容量を抑えるための --no-install-recommends オプション
        echo " && DEBIAN_FRONTEND=noninteractive apt install --no-install-recommends -y \$@ \\"; \
        echo " && apt clean \\"; \
        echo " && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*"; \
    } > /usr/local/bin/pkgadd.sh \
  && chmod +x /usr/local/bin/pkgadd.sh

# PDF出力のためにcalibreが必要
RUN pkgadd.sh calibre

RUN npm init --yes
RUN npm i -g honkit \
  # 日本語検索
  gitbook-plugin-search-pro-fixed \
  # "HonKitで公開" を非表示にする
  gitbook-plugin-hide-published-with \
  # 各見出しにアンカーを自動で付けてくれる
  gitbook-plugin-anchors \
  # 右上に目次（折りたたみ可能），右下にトップに戻るボタンの追加
  gitbook-plugin-navigator \
  # SUMMARYで折りたたみ可能なノードの先頭にアイコンが付く
  gitbook-plugin-collapsible-chapters \
  # {% hint style='(info|tip|danger|working)' %} 内容 {% endhint %}
  gitbook-plugin-hints \
  # コードスニペットにコピーボタンが表示
  gitbook-plugin-copy-code-button \
  # favicon
  gitbook-plugin-custom-favicon \
  # logo
  gitbook-plugin-insert-logo

# PDF出力の日本語フォント設定 (これがないと日本語表示不可)
ENV LANG ja_JP.UTF-8

# 07やさしさアンチック
COPY 07YasashisaAntique/fonts.conf /root/.config/fontconfig/
COPY 07YasashisaAntique/07YasashisaAntique.ttf /root/.local/share/fonts/

WORKDIR /srv/honkit
VOLUME /srv/honkit
EXPOSE 4000

CMD honkit serve || (honkit init && chmod -R +w /srv/honkit && honkit serve)
