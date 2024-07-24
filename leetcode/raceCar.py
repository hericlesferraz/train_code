from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])
        visited = set((0, 1))
        steps = 0

        while queue:
            for _ in range(len(queue)):
                position, speed = queue.popleft()

                if position == target:
                    print(steps)
                    return steps

                new_position = position + speed
                new_speed = speed * 2
                if (new_position, new_speed) not in visited:
                    queue.append((new_position, new_speed))
                    visited.add((new_position, new_speed))

                new_position = position
                new_speed = -1 if speed > 0 else 1
                if (new_position, new_speed) not in visited:
                    queue.append((new_position, new_speed))
                    visited.add((new_position, new_speed))

            steps += 1
        
        return -1

Solution().racecar(target=3)