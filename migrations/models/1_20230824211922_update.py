from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `organization` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50) NOT NULL  COMMENT '创建人',
    `updated_at` DATETIME(6) NOT NULL  COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50) NOT NULL  COMMENT '更新人',
    `business_code` VARCHAR(255) NOT NULL  COMMENT '业务编码',
    `db_version` INT NOT NULL  COMMENT '数据版本' DEFAULT 1,
    `org_level` INT NOT NULL  COMMENT '组织等级',
    `org_pid` VARCHAR(50) NOT NULL  COMMENT '上级组织id',
    `org_code` VARCHAR(50) NOT NULL  COMMENT '组织编码',
    `org_name` VARCHAR(50) NOT NULL  COMMENT '组织名称'
) CHARACTER SET utf8mb4 COMMENT='组织机构表';
        CREATE TABLE IF NOT EXISTS `organization_role` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50) NOT NULL  COMMENT '创建人',
    `updated_at` DATETIME(6) NOT NULL  COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50) NOT NULL  COMMENT '更新人',
    `business_code` VARCHAR(255) NOT NULL  COMMENT '业务编码',
    `db_version` INT NOT NULL  COMMENT '数据版本' DEFAULT 1,
    `organization_id` VARCHAR(50) NOT NULL,
    `role_id` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='组织机构-角色表';
        CREATE TABLE IF NOT EXISTS `role` (
    `id` VARCHAR(50) NOT NULL  PRIMARY KEY COMMENT 'id',
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `created_id` VARCHAR(50) NOT NULL  COMMENT '创建人',
    `updated_at` DATETIME(6) NOT NULL  COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `updated_id` VARCHAR(50) NOT NULL  COMMENT '更新人',
    `business_code` VARCHAR(255) NOT NULL  COMMENT '业务编码',
    `db_version` INT NOT NULL  COMMENT '数据版本' DEFAULT 1,
    `role_name` VARCHAR(255) NOT NULL  COMMENT '角色名',
    `role_code` VARCHAR(255) NOT NULL  COMMENT '角色编码'
) CHARACTER SET utf8mb4 COMMENT='角色表';
        ALTER TABLE `user` ADD `business_code` VARCHAR(255) NOT NULL  COMMENT '业务编码';
        ALTER TABLE `user` ADD `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `user` ADD `updated_id` VARCHAR(50) NOT NULL  COMMENT '更新人';
        ALTER TABLE `user` ADD `updated_at` DATETIME(6) NOT NULL  COMMENT '修改时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `user` ADD `created_id` VARCHAR(50) NOT NULL  COMMENT '创建人';
        ALTER TABLE `user` ADD `db_version` INT NOT NULL  COMMENT '数据版本' DEFAULT 1;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `user` DROP COLUMN `business_code`;
        ALTER TABLE `user` DROP COLUMN `created_at`;
        ALTER TABLE `user` DROP COLUMN `updated_id`;
        ALTER TABLE `user` DROP COLUMN `updated_at`;
        ALTER TABLE `user` DROP COLUMN `created_id`;
        ALTER TABLE `user` DROP COLUMN `db_version`;
        DROP TABLE IF EXISTS `organization`;
        DROP TABLE IF EXISTS `organization_role`;
        DROP TABLE IF EXISTS `role`;"""
