#include <memory>

#include "bst_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;
using std::vector;
// using std::next;
unique_ptr<BstNode<int>> RebuildBSTFromPreorder(
    const vector<int> &preorder_sequence)
{
  if (preorder_sequence.size() == 0)
  {
    return nullptr;
  }
  // TODO - you fill in here.
  auto transition = preorder_sequence.cbegin();
  auto currVal = std::next(transition);
  while (currVal != preorder_sequence.end() && *transition > *currVal)
  {

    currVal = std::next(currVal);
  }
  // std::next(transition);

  const vector<int> leftSubTree(transition + 1, currVal);
  const vector<int> rightSubTree(currVal, preorder_sequence.end());

  auto lnode = RebuildBSTFromPreorder(leftSubTree);
  auto rnode = RebuildBSTFromPreorder(rightSubTree);
  auto newBstNode = std::make_unique<BstNode<int>>(*transition, lnode, rnode);
  return newBstNode;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"preorder_sequence"};
  return GenericTestMain(args, "bst_from_preorder.cc", "bst_from_preorder.tsv",
                         &RebuildBSTFromPreorder, DefaultComparator{},
                         param_names);
}
