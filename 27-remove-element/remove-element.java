class Solution {
    public int removeElement(int[] nums, int val) {
        ArrayList<Integer> newlist = new ArrayList<>();
        for(int i : nums){
            if (i != val){
                newlist.add(i);
            }
        }

        for (int i = 0; i < newlist.size(); i++) {
            nums[i] = newlist.get(i);
        }

        return newlist.size();

    }
}