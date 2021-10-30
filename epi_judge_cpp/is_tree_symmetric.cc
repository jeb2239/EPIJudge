#include "binary_tree_node.h"
#include "test_framework/generic_test.h"

bool IsSymmetricRec(const unique_ptr<BinaryTreeNode<int>> &node1, const unique_ptr<BinaryTreeNode<int>> &node2)
{

  if (node1 == nullptr && node2 == nullptr)
  {
    return true;
  }
  if (node1 == nullptr)
  {
    return false;
  }
  if (node2 == nullptr)
  {
    return false;
  }

  if (node1->data != node2->data)
  {
    return false;
  }

  return IsSymmetricRec(node1->left, node2->right) && IsSymmetricRec(node1->right, node2->left);
}

bool IsSymmetric(const unique_ptr<BinaryTreeNode<int>> &tree)
{
  // you forgot to check for nullptr
  if (tree == nullptr)
  {
    return true;
  }
  return IsSymmetricRec(tree->right, tree->left);
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "is_tree_symmetric.cc", "is_tree_symmetric.tsv",
                         &IsSymmetric, DefaultComparator{}, param_names);
}
