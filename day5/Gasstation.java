/*
Фирма има N бензиностанции. 
Всяка седмица нейна цистерна извършва зареждането им тръгвайки от нейната централна складова база за горива, 
минавайки през всички бензиностанции и връщайки се обратно в нея. 
Помогнете на шофьора на цистерната да пресметне дължината на най-краткия път, по който той да извърши зареждането.

Input Format

На първият ред ще получите броя на тестовете – Т.
На първият ред от всеки тест ще получите броя на бензиностанциите N (централната база не се включва в N).
На следващият ред ще получите най-кратките разстояния S0,j от централната база до всички бензиностанции, подредени по нарастващ ред на номерата на бензиностанциите.
На следващите N – 1 реда ще получите най-кратките разстоянията Sk,j от поредната бензиностанция K (започвайки от първата във възходящ ред) 
до всички останали N – K бензиностанции с по-голям номер, подредени по нарастващ ред на номерата на бензиностанциите.
Всички пътища са двупосочни.
Не е възможно от една бензиностанция да стигнем до друга за по кратък път от този, който е зададен в тестовите данни за съответната двойка бензиностанции.

Constraints

1 ≤ Т ≤ 10 1 ≤ N ≤ 17 1 ≤ Si,j (разстояние между две бензиностанции – цяло число) ≤ 1500

Output Format

За всеки тест изведете на отделен ред дължината на най-краткия път, по който можем да минем през всички бензиностанции,
започвайки от централната база и завършвайки пак в нея.

Sample Input 0

1
4
11 13 22 7
15 18 17
11 11
22
Sample Output 0

58
Explanation 0

Най-краткият маршрут минава през бензиностанциите 1, 3, 2 и 4 и е с дължина 11 + 18 + 11 + 11 + 7 = 58
 */

import java.util.*;

public class Gasstation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        List<int[][]> cases = new ArrayList<>();
        
        for (int z = 0; z < t; z++) {
            int n = scanner.nextInt();
            int[][] matrix = new int[n + 1][n + 1];

            int[] baseDist = new int[n];
            for (int j = 0; j < n; j++) {
                baseDist[j] = scanner.nextInt();
            }

            for (int j = 1; j <= n; j++) {
                matrix[0][j] = matrix[j][0] = baseDist[j - 1];
            }

            for (int i = 1; i < n; i++) {
                int[] dists = new int[n - i];
                for (int j = 0; j < dists.length; j++) {
                    dists[j] = scanner.nextInt();
                }
                for (int j = i + 1; j <= n; j++) {
                    matrix[i][j] = matrix[j][i] = dists[j - i - 1];
                }
            }
            cases.add(matrix);
        }

        for (int[][] c : cases) {
            System.out.println(tsp(c));
        }
    }

    public static int tsp(int[][] connections) {
        int n = connections.length;
        int[][] dp = new int[1 << n][n];

        for (int[] row : dp) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }

        dp[1][0] = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    for (int j = 0; j < n; j++) {    // help :(
                        if ((mask & (1 << j)) == 0) {
                            int newMask = mask | (1 << j);
                            if (dp[mask][i] != Integer.MAX_VALUE && dp[mask][i] + connections[i][j] < Integer.MAX_VALUE) {
                                dp[newMask][j] = Math.min(dp[newMask][j], dp[mask][i] + connections[i][j]);
                            }
                        }
                    }
                }
            }
        }

        int minCost = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            minCost = Math.min(minCost, dp[(1 << n) - 1][i] + connections[i][0]);
        }

        return minCost;
    }
}