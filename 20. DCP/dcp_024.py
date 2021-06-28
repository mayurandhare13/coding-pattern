class LockingBinaryTreeNode:
    def __init__(self, val, left=None, right=None, parent=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self._is_locked = False
        self.lockedDescendantCount = 0
    

    def isLocked(self):
        return self._is_locked
    

    def _canLockOrUnlock(self):
        if self.lockedDescendantCount > 0:
            return False

        current = self.parent
        while current:
            if current.isLocked():
                return False
            current = current.parent

        return True


    def lock(self):
        if self._canLockOrUnlock():
            self._is_locked = True

            # update ancestors
            current = self.parent
            while current:
                current.lockedDescendantCount += 1
                current = current.parent

            return True

        return False


    # `lock` and `unlock` are both O(h) instead of O(m + h)
    def unlock(self):
        if self._canLockOrUnlock():
            self._is_locked = False

            # update ancestors
            current = self.parent
            while current:
                current.lockedDescendantCount -= 1
                current = current.parent

            return True

        return False

