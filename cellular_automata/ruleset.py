from frame import Frame


class RuleSet:
    # TODO: Rewrite.
    """
    Pure.
    Abstract.
    """

    pass


class TrivialRuleSet(RuleSet):
    def apply(self, frame) -> Frame:
        return Frame(frame.time + 1, frame.space)
