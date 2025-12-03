# 在这个文件里编写代码
import random

def simulate_point(prob_a):
    """模拟1分的争夺，prob_a是A选手得分概率"""
    return random.random() < prob_a

def simulate_game(prob_a):
    """模拟1局比赛，返回获胜方（'A'/'B'）和该局得分"""
    score_a, score_b = 0, 0
    while True:
        # 模拟得分
        if simulate_point(prob_a):
            score_a += 1
        else:
            score_b += 1

        # 判断该局胜负（11分制，领先至少2分）
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            winner = 'A' if score_a > score_b else 'B'
            return winner, score_a, score_b

def simulate_match(prob_a, best_of=3):
    """模拟一场比赛（三局两胜/五局三胜），返回获胜方和各局得分"""
    wins_a, wins_b = 0, 0
    game_results = []
    max_games = (best_of // 2) + 1  # 获胜所需局数

    while wins_a < max_games and wins_b < max_games:
        winner, sa, sb = simulate_game(prob_a)
        game_results.append((winner, sa, sb))
        if winner == 'A':
            wins_a += 1
        else:
            wins_b += 1

    match_winner = 'A' if wins_a > wins_b else 'B'
    return match_winner, game_results

def analyze_competition(prob_a, num_matches=1000):
    """模拟多场比赛，分析竞技规律（胜率、得分分布等）"""
    a_wins = 0
    all_scores = []

    for _ in range(num_matches):
        winner, game_results = simulate_match(prob_a)
        if winner == 'A':
            a_wins += 1
        # 记录每局得分
        for _, sa, sb in game_results:
            all_scores.append((sa, sb))

    # 统计结果
    win_rate_a = a_wins / num_matches * 100
    avg_score_a = sum(sa for sa, sb in all_scores) / len(all_scores)
    avg_score_b = sum(sb for sa, sb in all_scores) / len(all_scores)

    return {
        "A的胜率(%)": round(win_rate_a, 2),
        "单局A平均得分": round(avg_score_a, 2),
        "单局B平均得分": round(avg_score_b, 2),
        "模拟比赛场数": num_matches
    }

# 示例：A选手得分概率为0.55，模拟1000场比赛
if __name__ == "__main__":
    prob_a = 0.55  # A选手每分的获胜概率
    result = analyze_competition(prob_a, num_matches=1000)
    print("竞技分析结果：")
    for key, value in result.items():
        print(f"{key}: {value}")# 在这个文件里编写代码
