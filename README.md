file_manipulator.py では,コマンドライン引数として与えられるコマンドを用いて,
ファイルの操作を行う.

コマンド種類：
reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成する.

copy inputpath ouputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存する.

duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製する.

replace-string inputpath needle newstring: inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換える.

