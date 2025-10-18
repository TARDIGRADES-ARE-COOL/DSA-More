class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        
        ArrayList<Integer> finalist = new ArrayList<>();
        double fin;

        for (int i : nums1){
            finalist.add(i);

        }

        for (int y : nums2){
            finalist.add(y);
        }

        Collections.sort(finalist);
        

        if (finalist.size() %2 != 0 ){
            
            fin = finalist.get(finalist.size() / 2);
            return fin;

        }
        else{
        fin = (finalist.get(finalist.size() / 2)  + finalist.get(finalist.size() / 2 - 1)) / 2.0;

            return fin;
        }
        
    }
}