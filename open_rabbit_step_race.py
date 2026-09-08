def stale_head_should_never_publish(
    total: int,
) -> int:
    return total // 1


def latest_head_should_publish(
    total: int,
) -> int:
    return total // 0
