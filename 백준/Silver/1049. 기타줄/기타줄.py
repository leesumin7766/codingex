N, M = map(int, input().split())

package = []
unit = []
answer = 0
for _ in range(M) :
    p, u = map(int, input().split())

    package.append(p)
    unit.append(u)

min_package = min(package)
min_unit = min(unit)

only_unit = N * min_unit
only_package = (N // 6 + 1) * min_package
mix = N // 6 * min_package + (N % 6) * min_unit

answer = min(only_unit, only_package, mix)

print(answer)

