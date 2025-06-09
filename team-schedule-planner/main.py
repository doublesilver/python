import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

MAX_TEAM = 6
DAYS_IN_MONTH = 30  # 해당 월 날짜 수

class ScheduleApp:
    def __init__(self, master):
        self.master = master
        master.title("A조 / C조 팀원 스케줄표")

        self.team_entries = []
        self.schedule_cells = {}  # {(row, col): Entry}

        self.create_ui()

    def create_ui(self):
        # 팀원 입력 라벨 및 입력창
        tk.Label(self.master, text="팀원 이름 입력 (최대 6명)").grid(row=0, column=0, columnspan=DAYS_IN_MONTH+1, pady=10)

        for i in range(MAX_TEAM):
            entry = tk.Entry(self.master, width=15)
            entry.grid(row=i+1, column=0, padx=5, pady=3)
            self.team_entries.append(entry)

        # 날짜 라벨 생성
        today = datetime.today().replace(day=1)
        for day in range(DAYS_IN_MONTH):
            date_str = (today + timedelta(days=day)).strftime("%m/%d")
            tk.Label(self.master, text=date_str).grid(row=0, column=day+1)

        # 스케줄 입력 셀 생성
        for row in range(MAX_TEAM):
            for col in range(DAYS_IN_MONTH):
                e = tk.Entry(self.master, width=5)
                e.grid(row=row+1, column=col+1, padx=1, pady=1)
                self.schedule_cells[(row, col)] = e

        # 저장 버튼 (임시)
        tk.Button(self.master, text="저장하기 (다음 단계)", command=self.placeholder).grid(
            row=MAX_TEAM+2, column=0, columnspan=DAYS_IN_MONTH+1, pady=10
        )

    def placeholder(self):
        messagebox.showinfo("준비 중", "JSON/XLSX 저장 기능은 다음 단계에서 구현됩니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
