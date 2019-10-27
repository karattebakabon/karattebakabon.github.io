var FJShowHatenaBookmarkInfo = {};
FJShowHatenaBookmarkInfo.setup = function() {
    var script = document.createElement('script');
    script.type = "text/javascript";
    script.src = 'http://b.hatena.ne.jp/entry/json/?url=' + encodeURIComponent(location.href) + '&callback=FJShowHatenaBookmarkInfo.show';
    document.getElementsByTagName('head')[0].appendChild(script);
};
FJShowHatenaBookmarkInfo.show = function(data) {
    var elm = document.getElementById('hatena_bookmark');
    if (!data) {
        elm.innerHTML = '<p>まだ情報がありません。</p>';
        return;
    }
    var html = '<p>はてなブックマーク数 : <a href="' + data.entry_url + '">' + data.count + '</a></p>';
    if (data.count > 0) {
        html += '<ul>';
        for (var i = 0, j = data.bookmarks.length; i < j; i++) {
            var bookmark = data.bookmarks[i];
            html += '<li>';
            html += '<span class="bookmark-user">' +  bookmark.user + '</span>';
            html += ' <span class="bookmark-date">' +  bookmark.timestamp + '</span>';
            if (bookmark.comment) {
                html += '<br /><span class="bookmark-comment-title">コメント : </span>';
                html += '<span class="bookmark-comment-text">' +  bookmark.comment + '</span>';
            }
            if (bookmark.tags.length) {
                html += '<br /><span class="bookmark-tag-title">タグ : </span>';
                html += '<span class="bookmark-tag-title">' + bookmark.tags.join(', ') + '</span>';
            }
            html += '</li>';
        }
        html += '</ul>';
    }
    if (data.related.length) {
        html += '<p>関連するWebページ</p>';
        html += '<ul>';
        for (i = 0, j = data.related.length; i < j; i++) {
            var related = data.related[i];
            html += '<li>';
            html += '<a href="' + related.url + '">' + related.title + '</a>';
            html += '</li>';
        }
        html += '</ul>';
    }
    elm.innerHTML = html;
};
FJShowHatenaBookmarkInfo.setup();