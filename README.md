Python 環境設定快速入門

以下是在 Python 中建立虛擬環境、安裝必要的套件並執行應用程式的簡潔步驟。
步驟 1：建立虛擬環境

首先，我們將為您的專案建立一個隔離的環境。這有助於管理相依性並避免衝突。

python3 -m venv venv

    這會在目前的目錄中建立一個名為 "venv" 的新虛擬環境。

步驟 2：啟動虛擬環境

建立虛擬環境後，您需要啟動它才能使用它。

在 macOS 和 Linux 上：

source venv/bin/activate

在 Windows 上：

venv\Scripts\activate

    啟動環境後，您的命令提示字元或終端機將會顯示 "(venv)"，表示虛擬環境已啟用。

步驟 3：安裝套件

接下來，您需要使用 pip（Python 的套件管理器）安裝專案所需的套件。

pip install Flask

    此命令會安裝 Flask，這是一個用於建置 Web 應用程式的熱門 Python 框架。

        如果您有 requirements.txt 檔案，您可以使用以下命令安裝所有相依項：

        pip install -r requirements.txt

步驟 4：執行應用程式

現在，假設您有一個名為 app.py 的 Python 檔案，其中包含您的 Flask 應用程式。您可以使用以下命令執行它：

python app.py

    這將啟動您的 Flask 應用程式。

步驟 5：在瀏覽器中檢視

如果您的 Flask 應用程式設定正確，您應該可以在網頁瀏覽器中檢視它。

開啟您的網頁瀏覽器，然後前往以下 URL：

http://127.0.0.1:5000/

    如果應用程式正在執行中，您應該會看到您的 Web 應用程式的輸出。
