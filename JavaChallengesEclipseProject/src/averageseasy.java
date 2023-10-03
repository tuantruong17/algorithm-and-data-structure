import java.util.*;
public class averageseasy {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numCases = sc.nextInt();
        for (int i = 0; i < numCases; i++) {
            String filler = sc.nextLine();
            int numCs = sc.nextInt();
			int sumCs = 0;
            int numE = sc.nextInt();
            int sumE = 0;
            PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
            for (int j = 0; j < numCs; j++) {
				int val = sc.nextInt();
                pq.add(val);
				sumE += val;
            }
            for (int k = 0; k < numE; k++) {
                sumE += sc.nextInt();
            }
			double originalAvgE = (double) sumE / numE;
			int result = 0;
			while (pq.size() > 0 && (double) sumE / numE <= originalAvgE) {
                
				int lo = pq.poll();
				result += 1;
				sumE += lo;
				numE += 1;
			}
			System.out.println(result);
        }
    }
}