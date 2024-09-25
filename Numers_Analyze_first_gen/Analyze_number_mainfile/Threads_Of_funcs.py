class threads:
    # 为Downloader_get创建独立进程
    def thread_spider(self):
        self.thread_run=threading.Thread(target=download_function, name="thread1", daemon=True)
        self.thread_run.start()
    # 为搜索增加独立线程
    def thread_search_open_chrom(self):
        self.thread_open_url=threading.Thread(target=search_url, name="thread2", daemon=True)
        self.thread_open_url.start()
    # 为写入程序创建独立进程
    def thread_getfilename_and_wirtein(self):
        self.thread_get_filename_and_wirtein=threading.Thread(target=self.filename_get_and_writein, name="thread3", daemon=True)
        self.thread_get_filename_and_wirtein.start()
    # 创建下载按钮侦测
    def download_check_bind(self):
        self.downloader_run_result = self.button_download.bind(
            "<Button-1>", lambda event: self.thread_spider())
    # 为搜索按钮侦测
    def search_check_bind(self):
        self.search_run_result = self.button_search.bind(
            "<Button-1>", lambda event_1: self.thread_search_open_chrom())
    # 线程池
    def thread_pool_concurrent(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=None)
        self.threed_1 = self.thread_pool.submit(self.download_check_bind)
        self.thread_2 = self.thread_pool.submit(self.search_check_bind)
