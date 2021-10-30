#include <memory>
#include <vector>

#include "bst_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;
using std::vector;

void FindKLargestInBSTHelper(const unique_ptr<BstNode<int>>& tree,int k,vector<int>& v){

  if (tree==nullptr){
    return;
  }
  
  FindKLargestInBSTHelper(tree->right,k,v);
  if (v.size()==k){
    // before adding anything else to our result list
    // check that we have not already found k items
    // if we have then just terminate the search
    return;
  }
  v.push_back(tree->data);
    
  FindKLargestInBSTHelper(tree->left,k,v);
  
  
}

vector<int> FindKLargestInBST(const unique_ptr<BstNode<int>>& tree, int k) {
  // TODO - you fill in here.
  vector<int> v;
  FindKLargestInBSTHelper(tree,k,v);
  return v;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree", "k"};
  return GenericTestMain(args, "k_largest_values_in_bst.cc",
                         "k_largest_values_in_bst.tsv", &FindKLargestInBST,
                         UnorderedComparator{}, param_names);
}
