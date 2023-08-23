from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `user` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id',
    `name` VARCHAR(255) NOT NULL  COMMENT '用户名',
    `account` VARCHAR(255) NOT NULL  COMMENT '账号',
    `pwd` VARCHAR(255) NOT NULL  COMMENT '密码',
    `collect` LONGTEXT   COMMENT '用户收藏',
    KEY `idx_user_name_76f409` (`name`)
) CHARACTER SET utf8mb4 COMMENT='用户表';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
