#include <memory>

#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;

bool IsBinaryTreeBSTBound(const unique_ptr<BinaryTreeNode<int>> &tree, int lowerbound, int upperbound)
{

  if (tree == nullptr)
  {
    return true;
  }

  if (!(lowerbound <= tree->data && tree->data <= upperbound))
  {
    return false;
  }

  bool lbool = IsBinaryTreeBSTBound(tree->left, lowerbound, tree->data);
  bool rbool = IsBinaryTreeBSTBound(tree->right, tree->data, upperbound);

  return lbool && rbool;
}

bool IsBinaryTreeBST(const unique_ptr<BinaryTreeNode<int>> &tree)
{
  // TODO - you fill in here.

  return IsBinaryTreeBSTBound(tree, std::numeric_limits<int>::min(), std::numeric_limits<int>::max());
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "is_tree_a_bst.cc", "is_tree_a_bst.tsv",
                         &IsBinaryTreeBST, DefaultComparator{}, param_names);
}
