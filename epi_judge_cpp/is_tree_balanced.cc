#include "binary_tree_node.h"
#include "test_framework/generic_test.h"


std::pair<int,bool> IsBalancedRec(const unique_ptr<BinaryTreeNode<int>>& tree){

  if(tree==nullptr){
      return std::make_pair(0,true);
    }

    auto leftPack=IsBalancedRec(tree->left);
    auto rightPack=IsBalancedRec(tree->right);
    if (leftPack.second==false || rightPack.second==false){
      return std::make_pair(0,false);
    }
    if(abs(leftPack.first-rightPack.first) > 1){
      return std::make_pair(0,false);
    }

    int height = std::max(leftPack.first,rightPack.first)+1;
    return std::make_pair(height,true);

}

bool IsBalanced(const unique_ptr<BinaryTreeNode<int>>& tree) {
  
  
  return IsBalancedRec(tree).second;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "is_tree_balanced.cc", "is_tree_balanced.tsv",
                         &IsBalanced, DefaultComparator{}, param_names);
}
