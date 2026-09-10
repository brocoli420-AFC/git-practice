"""成绩统计小工具 —— Git 练手用的素材。"""


def average(scores: list[float]) -> float:
    """返回平均分，空列表返回 0.0。"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def max_score(scores: list[float]) -> float:
    """返回最高分，空列表返回 0.0。"""
    return max(scores) if scores else 0.0


def pass_rate(scores: list[float], line: float = 60.0) -> float:
    """返回及格率（百分比），空列表返回 0.0。"""
    if not scores:
        return 0.0
    passed = sum(1 for s in scores if s >= line)
    return passed / len(scores) * 100


def main() -> None:
    scores = [88.5, 92.0, 76.5, 95.0, 81.0]
    print(f"成绩: {scores}")
    print(f"平均分: {average(scores):.2f}")
    print(f"最高分: {max_score(scores):.2f}")
    print(f"及格率: {pass_rate(scores):.1f}%")


if __name__ == "__main__":
    main()
