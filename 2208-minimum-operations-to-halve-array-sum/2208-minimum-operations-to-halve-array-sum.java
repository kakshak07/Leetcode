class Solution {
    public int halveArray(int[] nums) {
        PriorityQueue<Double> pq = new PriorityQueue<>((a, b) -> Double.compare(b, a));

		double sum = 0;

		// initialize queue and sum
		for (int n : nums) {
			pq.add(Double.valueOf(n));
			sum += n;
		}

		// get half of sum
		double half = sum / 2;

		// count variable for the answer
		int count = 0;

		// use sum > half so the count will not add an extra value, also takes care of  
		// other cases like [1, 2] where the sum is near the half
		while (sum > half) {
			double currMax = pq.poll(); // get curr max
			currMax /= 2; // get half of curr max
			sum -= currMax; // subtract the curr max to the sum
			pq.offer(currMax); // place back the halfed max to the queue
			count++;// increment answer
		}

		return count;
    }
}