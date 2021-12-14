CREATE TABLE IF NOT EXISTS Trades (
   pk PRIMARY KEY,
   type TEXT NOT NULL,
   subAccount INTEGER,
   settlementDate  TEXT,    -- 2021-11-30T16:19:24+0000
   orderId TEXT,                    -- oid.n relates n TRADES in spread
   netAmount FLOAT,
   transactionDate TEXT,    -- 2021-11-30T16:19:24+0000
   orderDate TEXT,    -- 2021-11-30T16:19:24+0000
   transactionSubType TEXT,  TEXT,    -- SL, ...
   transactionId TEXT,
   cashBalanceEffectFlag  TEXT  -- true or flase
   description TEXT                     -- SELL TRADE or BUY TRADE
)