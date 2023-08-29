from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `organization` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id' DEFAULT '1696328061487816704',
    `created_at` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50)   COMMENT '创建人' DEFAULT '',
    `updated_at` DATETIME(6)   COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50)   COMMENT '更新人' DEFAULT '',
    `business_code` VARCHAR(255)   COMMENT '业务编码' DEFAULT '',
    `db_version` INT   COMMENT '数据版本' DEFAULT 1,
    `org_level` INT NOT NULL  COMMENT '组织等级',
    `org_pid` VARCHAR(50) NOT NULL  COMMENT '上级组织id',
    `org_code` VARCHAR(50) NOT NULL  COMMENT '组织编码',
    `org_name` VARCHAR(50) NOT NULL  COMMENT '组织名称'
) CHARACTER SET utf8mb4 COMMENT='组织机构表';
CREATE TABLE IF NOT EXISTS `role` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id' DEFAULT '1696328061487816704',
    `created_at` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50)   COMMENT '创建人' DEFAULT '',
    `updated_at` DATETIME(6)   COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50)   COMMENT '更新人' DEFAULT '',
    `business_code` VARCHAR(255)   COMMENT '业务编码' DEFAULT '',
    `db_version` INT   COMMENT '数据版本' DEFAULT 1,
    `role_name` VARCHAR(255) NOT NULL  COMMENT '角色名',
    `role_code` VARCHAR(255) NOT NULL  COMMENT '角色编码'
) CHARACTER SET utf8mb4 COMMENT='角色表';
CREATE TABLE IF NOT EXISTS `organization_role` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id' DEFAULT '1696328061487816704',
    `created_at` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50)   COMMENT '创建人' DEFAULT '',
    `updated_at` DATETIME(6)   COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50)   COMMENT '更新人' DEFAULT '',
    `business_code` VARCHAR(255)   COMMENT '业务编码' DEFAULT '',
    `db_version` INT   COMMENT '数据版本' DEFAULT 1,
    `organization_id` VARCHAR(50) NOT NULL,
    `role_id` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='组织机构-角色表';
CREATE TABLE IF NOT EXISTS `user` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id' DEFAULT '1696328061487816704',
    `created_at` DATETIME(6)   COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50)   COMMENT '创建人' DEFAULT '',
    `updated_at` DATETIME(6)   COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50)   COMMENT '更新人' DEFAULT '',
    `business_code` VARCHAR(255)   COMMENT '业务编码' DEFAULT '',
    `db_version` INT   COMMENT '数据版本' DEFAULT 1,
    `name` VARCHAR(255) NOT NULL  COMMENT '用户名',
    `account` VARCHAR(255) NOT NULL  COMMENT '账号',
    `pwd` VARCHAR(255)   COMMENT '密码',
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
