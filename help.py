
from subprocess import call
hashes = ["098e8bb84d396113d3f902fa0be0c76375506b07",
          "094f1aad3f174e872ee23c2a8c5443381ed7df39",
          "11816f7d0fe6211776ba0a8782667126b6b23999",
          "150052bfac446d6210e804f4089cb9b0115394d5",
          "1e09c3be682eb97a79ff306c381e447031ff8916",
          "23f37f303ad90e8f1849e65789d8d91095d2e88b",
          "25bfda6a0d37a45d803d2188edeae0d4afd2335b",
          "2838f3f6b6d89e43ef70fca02e21dda32f6b883a",
          "33ec4ea7966f7fb6fe30c74ab8bcfae4ff77319e",
          "341c99dff97b8109474887a00124c19a479b6b60",
          "367dbfae9c1cb904fd4b5a2829b6d3b857fb6999",
          "4396e6540d0459fed08d516b440a47be4d85130e",
          "4b48dd96819244d2560749cf1518930a84071def",
          "4b3e48c1daa8d9b8fcb5ab65a8730b6b6fdce7e1",
          "4c08684a93fe40ca2590c180a46c87bc13c32f9a",
          "509ee66703ffe93f606a28310eea4147b9a2ad06",
          "517fcc5f0f1b4e8ecbcdafecebe6b22281e18ce1",
          "534a278c778decc64d17ea5d978a0c71bbea28cf",
          "56a65786072f3d64efb44033be976835d2f22d69",
          "58898aa4d0c6ad03db25d8f890294a087ee48797",
          "5a389f11f4d58cdb47509827ccf6abc238e2e0ac",
          "5b14393c55dfd5000c5f68e7e2739802df6988b8",
          "5b4b38795d8bf1d7e13a3f7c18c078350afb051f",
          "654987fe1e6f87a6a2c575e10d52f25a2b0675f3",
          "6ccec37204a3bf01117b315224a9f9639edd75b3",
          "6c196af4ae3e774aac978b6fd85a37ab32a9361f",
          "6f2668c80945a6982d4a7158d95c4cf0d8c2698a",
          "759c44113a637c80be6b9265e8cc674d98f086f4",
          "7796791af64f59f9623cca09929f96cc70f6ab89",
          "77814cbb01d9b6762a18ac7ff4d94a1cba403a01",
          "7703b449ad44a94fb99de9d0670baa3ffb16efba",
          "7be2bad7615e5f7894c2d02f1cd226552d6794ca",
          "7baa316bb680d0dbc4b5f86cb8f44a338ad16e26",
          "7e555ab092cda8b9d8ebc5d009b19c5173f220f1",
          "846ca11f22b29afaa88a6967ac4a0b58fd89ff6a",
          "84002822f45e7508b3fb9614eb297a6ee591b8e1",
          "8b8b7d54698107b6fa7045a9259f7ba4441ac9dc",
          "8ee568e3a22341a592b7da8fb0fc87a5bbdd5f62",
          "8f551ed6288cd32a097a4b86ff9a2844a9e27c40",
          "913267c978291a7854491c8c34dad1a86c446ab2",
          "9965f262be0244f9b22a3c0ac232eedce6624f6f",
          "a254bb090fabef96a1fb4624bd1cbd851c54b8a0",
          "a4ca9308617c19435919a4c2067a755ad86dca12",
          "a6ea131ec84d822f4f3ed84fd2ec419b6f942ace",
          "acd6359cb6d3ad5f69649b5b32373342ab1dd8e7",
          "ab7b7a8cf8c09a1011f4fc3611bc988bdc935aef",
          "afd5a2a008e3a9083f2667f95f930796718806ed",
          "b72bae108e7fa0114f276bfba44127e7613a8df4",
          "baf5dccd3fab1f56cd7e2f7950573545eb8782bf",
          "c2c23e1c9cdf421a0c5633e7346cb193c67a38e1",
          "c650b5fa51760a9cf45db2cb382e56c951e11bb1",
          "ce1757dfb5018175ff60ddf7ba76336e79e1cb59",
          "cfc49887d7d870d343debfbee2e192ffb2854411",
          "d6505aac4c9c7fff0d62499ac99539b6ee0831dd",
          "d72d89c500d4076f64eb044876e933c055c36ece",
          "e5525a8eaa2e859ba84af375524d445bb20a01a4",
          "e5a8294e607fc1bd5b5410c0d2f870c751b51583",
          "e67cb29b743d890d5d846385548a6dbde693aadc",
          "e8b1023b714039afc3db1aea07ee9220beba89b1",
          "e89d7cbaa6d55266cd43d2503b65a553a25a2b37",
          "e987550e246c3756fff5879bf1dc9b26fd986c49",
          "f0f77b8f69f05f500fa6d3ba4b0a82a2bef5b9cd",
          "f055d0127f41fc6e5b3467b6e036278df2f3ec51",
          "f2f717f5e6560e40c5122002b70745a18fdf731a"]


filename = "file"
i = 1
for c in hashes:
    f = open(filename + str(i), "wb")
    call(["git", "show", c], stdout=f)
    i += 1