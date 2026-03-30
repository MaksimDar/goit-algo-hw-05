import sys

def parse_log_line(line: str) -> dict:
    line_parts = line.strip().split(" ", 3)
    if len(line_parts) < 4:
        return None 
    log_dict = {"date": line_parts[0], "time": line_parts[1], "level": line_parts[2], "message": line_parts[3]}
    return log_dict
    

def load_logs(file_path: str) -> list:
    lict_logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as fh:
            for line in fh:
                parsed = parse_log_line(line)
                lict_logs.append(parsed)
                
    except FileNotFoundError:
        print(f'{file_path} is not found')

    return lict_logs

def filter_logs_by_level(logs: list, level: str):
    return list(filter(lambda log: log["level"] == level, logs ))

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level:<17}| {counts.get(level, 0)}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 task_3.py logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if level_filter:
        level_filter = level_filter.upper()
        filtered = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter}':")

        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")