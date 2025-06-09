from datetime import datetime, timedelta
import random

def assign_schedule(team_members, rest_days, last_month_roles, year, month):
    """
    team_members: ['홍길동', '김영희', ...]
    rest_days: {'홍길동': ['2025-06-01', ...], ...}
    last_month_roles: {'홍길동': 'A', '김영희': 'C', ...}
    return: {'홍길동': {'2025-06-01': 'A', '2025-06-02': 'C', ...}, ...}
    """
    result = {name: {} for name in team_members}
    consecutive_days = {name: 0 for name in team_members}
    assigned_dates = {name: [] for name in team_members}

    # 날짜 리스트 생성
    start_date = datetime(year, month, 1)
    days_in_month = 30  # 간단히 30일로 고정 (추후 개선 가능)
    date_list = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days_in_month)]

    for date in date_list:
        available_A = get_available_members('A', team_members, rest_days, result, consecutive_days, assigned_dates, date, last_month_roles)
        available_C = get_available_members('C', team_members, rest_days, result, consecutive_days, assigned_dates, date, last_month_roles)

        if len(available_A) < 2 or len(available_C) < 2:
            raise Exception(f"{date}에 조 배정을 만족할 수 없습니다.")

        # 무작위 선택 (추후 더 정교한 로직으로 교체 가능)
        selected_A = random.sample(available_A, 2)
        selected_C = random.sample(available_C, 2)

        for name in selected_A:
            result[name][date] = 'A'
            assigned_dates[name].append(date)
            consecutive_days[name] = count_consecutive_days(assigned_dates[name])

        for name in selected_C:
            result[name][date] = 'C'
            assigned_dates[name].append(date)
            consecutive_days[name] = count_consecutive_days(assigned_dates[name])

    return result

def get_available_members(role, members, rest_days, result, consecutive_days, assigned_dates, date, last_month_roles):
    available = []
    for name in members:
        if date in rest_days.get(name, []):
            continue
        if date in result[name]:
            continue
        if consecutive_days[name] >= 5:
            continue
        # 형평성 고려 (지난달 A면 이번달 C 우선)
        if last_month_roles.get(name) == 'A' and role == 'A':
            continue
        if last_month_roles.get(name) == 'C' and role == 'C':
            continue
        available.append(name)
    return available

def count_consecutive_days(date_list):
    if not date_list:
        return 0
    # 정렬 후 연속 일 수 계산
    dates = sorted([datetime.strptime(d, '%Y-%m-%d') for d in date_list])
    count = 1
    max_count = 1
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count
