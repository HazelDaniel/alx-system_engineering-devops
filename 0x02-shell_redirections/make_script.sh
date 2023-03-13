#!/bin/bash

for i in $*; do
  echo '#!/bin/bash' > $i;
  chmod u+x $i;
done
