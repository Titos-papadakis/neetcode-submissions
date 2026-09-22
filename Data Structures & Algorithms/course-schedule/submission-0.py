class Solution:

  def canFinish(
      self, numCourses: int, prerequisites: list[list[int]]
  ) -> bool:
    # 1. Ftiaxneis grafo kai metras proapaitoumena
    adj = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
      adj[prereq].append(course)
      in_degree[course] += 1

    # 2. Vazeis sti lista osa den exoun proapaitoumena (in_degree == 0)
    free = [i for i in range(numCourses) if in_degree[i] == 0]

    # 3. Ksekleidoneis ta epomena mathimata
    for node in free:
      for neighbor in adj[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
          free.append(neighbor)

    # 4. Elegxos: perases ola ta mathimata;
    return len(free) == numCourses