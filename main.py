"""成绩统计小工具 —— Git 练手用的素材。"""


def average(scores: list[float]) -> float:
    """返回平均分，空列表返回 0.0。"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def max_score(scores: list[float]) -> float:
    """返回最高分，空列表返回 0.0。"""
    return max(scores) if scores else 0.0


def main() -> None:
    scores = [88.5, 92.0, 76.5, 95.0, 81.0]
    print(f"成绩: {scores}")
    print(f"平均分: {average(scores):.2f}")
    print(f"最高分: {max_score(scores):.2f}")


if __name__ == "__main__":
    main()
