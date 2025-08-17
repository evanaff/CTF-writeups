# FreeFlag
## Hacktoday 2025

This was my first blockchain challenge. The description did not provide any useful hints, only a link to the blockchain launcher and a zip file containing `Setup.sol` and `Warmup.sol`.

<img width="1074" height="764" alt="Screenshot From 2025-08-12 15-32-59" src="https://github.com/user-attachments/assets/5ff6c8ca-f0ca-483e-a823-d2316f0d887b" />

The first step was to submit a solution. I could obtain it by executing the provided command on the blockchain launcher. Once I got the solution, I was able to launch the blockchain instance and receive the credentials.

I used a tool called [Foundry](https://getfoundry.sh/). I created a Foundry project by running the command: `forge init`, then add `Setup.sol` and `Warmup.sol` to `/script`.

Next, I prepared a .env file containing the credential variables (RPC_URL, PRIVKEY, SETUP, WALLET). By running source .env, I exported all variables into the shell environment. With that, I could start interacting with the contract using cast. For example:
```foundry
cast call $SETUP "isSolved()(bool)" --rpc-url $RPC_URL
false
```

To solve the challenge I need to check the condition defined on `Setup.sol`.

```solidity
function isSolved() external view returns (bool) {
    return warmup.solved();
}
```

This indicated that the actual solving logic was in `Warmup.sol`.

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Warmup {
    bool public solved;
    constructor() {

        bytes memory _byte = hex"608060405234801561000f575f5ffd5b5060043610610034575f3560e01c8063799320bb14610038578063f492302614610056575b5f5ffd5b610040610072565b60405161004d91906100d5565b60405180910390f35b610070600480360381019061006b9190610125565b610083565b005b5f5f9054906101000a900460ff1681565b611092821480156100965750620aa28981145b61009e575f5ffd5b60015f5f6101000a81548160ff0219169083151502179055505050565b5f8115159050919050565b6100cf816100bb565b82525050565b5f6020820190506100e85f8301846100c6565b92915050565b5f5ffd5b5f819050919050565b610104816100f2565b811461010e575f5ffd5b50565b5f8135905061011f816100fb565b92915050565b5f5f6040838503121561013b5761013a6100ee565b5b5f61014885828601610111565b925050602061015985828601610111565b915050925092905056fea264697066735822122097d365bee5aca894d5c1fd3462418a123ca24137e88143721acca112ff90f0f464736f6c634300081c0033";
        assembly {
            return(add(_byte, 0x20), mload(_byte))
        }
    }

    function solve(uint256 a, uint256 b) external {
        require((a == 1) && (b == 2));
        solved = true;
    }
}
```

There is function called solve that use 2 parameters. To solve it, I needed to pass 2 parameters (a = 1, b = 2). I tried to call it using cast but fails. But I noticed a long hex string inside the constructor, which turned out to be raw bytecode. After some search I know that the bytecode is a compiled codes. I decompile it using https://ethervm.io/decompile.

```solidity
...
    function func_006B(var arg0, var arg1) {
        var var0 = arg0 == 0x1092;
    
        if (!var0) {
            if (!var0) { revert(memory[0x00:0x00]); }
        
        label_009E:
            storage[0x00] = (storage[0x00] & ~0xff) | 0x01;
            return;
        } else if (arg1 == 0x0aa289) { goto label_009E; }
        else { revert(memory[0x00:0x00]); }
    }
...
```

From the decompiled code, the condition required passing the values `0x1092` and `0x0aa289` to the function. So I call it using cast.

<img width="1246" height="387" alt="Screenshot From 2025-08-17 15-22-06" src="https://github.com/user-attachments/assets/48adf50f-0985-4b9b-b051-95962142c1bf" />

*Note : $CHALL is the same as $SETUP.

<img width="491" height="42" alt="Screenshot From 2025-08-17 15-23-03" src="https://github.com/user-attachments/assets/1f698ed9-4e00-4c32-81fd-c11e9baebd6c" />

`isSolved()` is now has `true` value, which means I can get the flag by access it through `flag` button on blockchain launcher before.
