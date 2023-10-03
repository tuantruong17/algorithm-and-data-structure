import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/** Solved in class together - https://open.kattis.com/problems/peragrams 
 * 
 * Sketch of algorithm:
 *  1. do a frequency count of the letters used in the words
 *  2. see how many of the frequencies are odd
 *  3. it's okay to have 0 or 1 odd frequencies to make a palindrome,
 *     but every odd frequency beyond that will require removing one letter.
 * 
 * @author Forrest Stonedahl
 */
// 
public class peragrams {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in); 
		String word = input.next();
		
		Map<Character,Integer> counts = new HashMap<>();
		
		for (char ch : word.toCharArray()) {
			counts.put(ch, counts.getOrDefault(ch, 0)+1);
		}
		
		int numOdd = 0;
		for (char ch : counts.keySet()) {
			int count = counts.get(ch);
			if (count % 2 == 1) {
				numOdd++;
			}
		}
		if (numOdd > 0) {
			System.out.println(numOdd - 1);
		} else {
			System.out.println(0);
		}
	}

}
