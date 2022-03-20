//SPDX-License-Identifier: MIT

pragma solidity >=0.8.0;

contract SimpleStorage {
    uint256 integer_variable;

    function get_int() public view returns(uint256) {
        return integer_variable;
    }

    function set_int(uint256 new_int) public {
        require(integer_variable != new_int);
        integer_variable = new_int;
    }
}